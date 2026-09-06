from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import luminous_sign
from spirit.game.card_effects.support_common import remove_self_from_play

card = PokemonCardDef(
    guid="7d3d149a-981d-50b7-b994-4a3168465463",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowthex.Name",
    display_name="Meowth ex",
    searchable_by=["Meowth ex", "Basic", "ex", "Meowthex"],
    subtypes=["Basic", "ex"],
    collector_number=62,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=52,
    abilities=[
        Ability(
            title="Last-Ditch Catch",
            game_text='Once during your turn, when you play this Pokémon from your hand onto your Bench, you may use this Ability. Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck. You can\'t use more than 1 Ability that has "Last-Ditch" in its name each turn.',
            trigger=Triggers.ON_PLAY,
            shared_once_per_turn="Last-Ditch",
            effect=luminous_sign,
        ),
        Attack(
            title="Tuck Tail",
            game_text="Put this Pokémon and all attached cards into your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=remove_self_from_play("hand"),
        ),
    ],
)
