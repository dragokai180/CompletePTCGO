from spirit.game.data_utils import PokemonCardDef, Ability, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class _SeasonedSkillPassive(Passive):
    """Discount Blood Moon, even when another effect has changed its cost."""

    def modify_attack_cost_for_attack(self, cost, pokemon, carrier, board, attack):
        if carrier is not pokemon or getattr(attack, "title", "") != "Blood Moon":
            return cost
        owner = carrier.owning_player_id
        opponent = next((p for p in board.player_ids if p != owner), None)
        if opponent is None:
            return cost

        discount = board.prizes_taken(opponent)
        if discount <= 0:
            return cost

        remaining = cost.get("Colorless", 0) - discount
        if remaining > 0:
            cost["Colorless"] = remaining
            return cost
        # Remove empty cost component if fully discounted.
        cost.pop("Colorless", None)
        return cost


card = PokemonCardDef(
    guid="d4ab86fa-876c-433d-b80f-e0a0eaeeff33",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BloodmoonUrsalunaex.Name",
    display_name="Bloodmoon Ursaluna ex",
    searchable_by=["Bloodmoon Ursaluna ex", "Basic", "ex", "BloodmoonUrsalunaex"],
    subtypes=["Basic", "ex"],
    collector_number=141,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=901,
    abilities=[
        Ability(
            title="Seasoned Skill",
            game_text=(
                "Blood Moon used by this Pokémon costs [C] less for each "
                "Prize card your opponent has taken."
            ),
            passive=_SeasonedSkillPassive(),
        ),
        Attack(
            title="Blood Moon",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 5},
            damage=240,
            locks_next_turn=True,
        ),
    ],
)

