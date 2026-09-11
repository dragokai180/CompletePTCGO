from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive

card = PokemonCardDef(
    guid="1adae36b-b635-593b-af1f-10f58caa4e1d",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb","Basic","Spiritomb"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    abilities=[
        Ability(
            title="Sealing Scream",
            game_text="Each player can't play any ACE SPEC cards from his or her hand.",
            passive=bw_legacy_passive("Each player can't play any ACE SPEC cards from his or her hand."),
        ),
        Attack(
            title="Hexed Mirror",
            game_text="Shuffle your hand into your deck. Then, draw a number of cards equal to the number of cards in your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=bw_legacy_attack,
        ),
    ],
)
