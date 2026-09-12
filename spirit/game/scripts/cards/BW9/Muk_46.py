from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="dfd63c0d-5216-5176-9686-923779e05808",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name",
    display_name="Muk",
    searchable_by=["Muk","Stage 1","Muk","Team Plasma"],
    subtypes=["Stage 1","Team Plasma"],
    collector_number=46,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    abilities=[
        Attack(
            title="Poison Suction",
            game_text="If the Defending Pokémon is Poisoned, heal 60 damage from this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Sludge Crash",
            game_text="Flip a coin until you get tails. For each heads, discard an Energy attached to the Defending Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=bw_legacy_attack,
        ),
    ],
)
