from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive


class SphericalShieldPassive(Passive):
    """Prevent all damage from and effects of opposing attacks done to your
    Benched Pokémon."""

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        return (
            calc.target.owning_player_id == carrier.owning_player_id
            and not is_in_active_spot(calc.target)
        )

    def blocks_attack_effects(self, target, carrier):
        return (
            target.owning_player_id == carrier.owning_player_id
            and not is_in_active_spot(target)
        )


card = PokemonCardDef(
    guid="7be6eeac-32bd-5b6b-ba2e-8f41ef35e69c",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rabsca.Name",
    display_name="Rabsca",
    searchable_by=["Rabsca","Stage 1","Rabsca"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    family_id=953,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rellor.Name",
    abilities=[
        Ability(
            title="Spherical Shield",
            game_text="Prevent all damage from and effects of attacks from your opponent's Pokémon done to your Benched Pokémon.",
            passive=SphericalShieldPassive(),
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 30, base=10),
        ),
    ],
)
