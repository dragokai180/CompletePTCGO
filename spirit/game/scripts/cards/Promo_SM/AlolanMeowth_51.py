from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9d8d395d-4dcd-59ca-ae40-372f54faf01f',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMeowth.Name',
    display_name='Alolan Meowth',
    searchable_by=['Alolan Meowth', 'Basic', 'AlolanMeowth'],
    subtypes=['Basic'],
    collector_number=51,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=52,
    abilities=[
        Attack(
            title='Nasty Plot',
            game_text='Flip a coin. If heads, search your deck for a card and put it into your hand. Then, shuffle your deck.',
            cost={},
            effect=standard_attack,
        ),
        Attack(
            title='Scratch',
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)
