from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import ignore_effects_attack, snipe_attack

card = PokemonCardDef(
    guid="cb0e78f0-767e-5975-ad95-451cf893ae56",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaStarmieex.Name",
    display_name="Mega Starmie ex",
    searchable_by=["Mega Starmie ex", "Stage 1", "ex", "SV_Mega", "MegaStarmieex"],
    subtypes=["Stage 1", "ex", "SV_Mega"],
    collector_number=21,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Jetting Blow",
            game_text="This attack also does 50 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            damage=120,
            effect=snipe_attack(50, also_base=True),
        ),
        Attack(
            title="Nebula Beam",
            game_text="This attack's damage isn't affected by Weakness or Resistance, or by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=210,
            effect=ignore_effects_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)
