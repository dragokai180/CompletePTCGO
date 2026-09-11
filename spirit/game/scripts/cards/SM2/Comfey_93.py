from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='21fcddc6-697c-5923-b9b1-3d7e21e78f49',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Comfey.Name',
    display_name='Comfey',
    searchable_by=['Comfey', 'Basic', 'Comfey'],
    subtypes=['Basic'],
    collector_number=93,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=764,
    abilities=[
        Ability(
            title='Flower Shield',
            game_text="Each of your Pokémon that has any Fairy Energy attached to it can't be affected by any Special Conditions. Remove any Special Conditions affecting those Pokémon.",
            passive=standard_passive("Each of your Pokémon that has any Fairy Energy attached to it can't be affected by any Special Conditions. Remove any Special Conditions affecting those Pokémon."),
        ),
        Attack(
            title='Sweet Kiss',
            game_text='Your opponent draws a card.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
