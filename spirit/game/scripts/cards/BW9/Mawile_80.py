from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="8435d63b-cb60-55c9-8480-690b9afdc5aa",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name",
    display_name="Mawile",
    searchable_by=["Mawile","Basic","Mawile"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Astonish",
            game_text="Flip a coin. If heads, choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into his or her deck.",
            cost={PokemonTypes.METAL: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Big Ol' Bite",
            game_text="Heal 30 damage from this Pokémon. The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=bw_legacy_attack,
        ),
    ],
)
