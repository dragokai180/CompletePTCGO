from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7ede7947-92da-5b4b-9598-866b6127c0a5',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name',
    display_name='Groudon',
    searchable_by=['Groudon', 'Basic', 'Groudon'],
    subtypes=['Basic'],
    collector_number=99,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    attributes={200790: {'type': 'string', 'value': 'SL4'}},
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=383,
    abilities=[
        Attack(
            title='Volcano Stomp',
            game_text="Flip a coin. If heads, discard the top 4 cards of your opponent's deck. If tails, discard the top 4 cards of your deck.",
            cost={PokemonTypes.FIGHTING: 4},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
