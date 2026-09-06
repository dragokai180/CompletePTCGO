from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import damage_per, count_bench
from spirit.game.session.passives import Passive


class _FairyZonePassive(Passive):
    """Opponent's Dragon Pokémon in play are Weak to Psychic (×2)."""

    def modify_weakness(self, calc, carrier):
        if calc.target.owning_player_id == carrier.owning_player_id:
            return
        types = calc.target.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.DRAGON.value not in types:
            return
        calc.weak_types = [PokemonTypes.PSYCHIC.value]
        calc.weakness_multiplier = 2


card = PokemonCardDef(
    guid="77f07519-2a6e-5626-898e-e0c5f368d52e",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LilliesClefairyex.Name",
    display_name="Lillie's Clefairy ex",
    searchable_by=["Lillie's Clefairy ex", "Basic", "ex", "LilliesClefairyex"],
    subtypes=["Basic", "ex"],
    collector_number=56,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=35,
    abilities=[
        Ability(
            title="Fairy Zone",
            game_text="The Weakness of each of your opponent's Dragon Pokémon in play is now Psychic. (Apply Weakness as ×2.)",
            passive=_FairyZonePassive(),
        ),
        Attack(
            title="Full Moon Rondo",
            game_text="This attack does 20 more damage for each Benched Pokémon (both yours and your opponent's).",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_bench("both"), 20, base=20),
        ),
    ],
)
