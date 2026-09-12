from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="e5333328-1b93-5991-b322-dcff8161defb",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krookodile.Name",
    display_name="Krookodile",
    searchable_by=["Krookodile","Stage 2","Krookodile","Team Plasma"],
    subtypes=["Stage 2","Team Plasma"],
    collector_number=70,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    abilities=[
        Attack(
            title="Piston Headbutt",
            game_text="Move an Energy attached to the Defending Pokémon to 1 of your opponent's Benched Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
