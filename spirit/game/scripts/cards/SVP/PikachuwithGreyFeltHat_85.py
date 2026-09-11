from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7cb7de4f-a29b-50b2-ab8f-fb82fe540351',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PikachuwithGreyFeltHat.Name',
    display_name='Pikachu with Grey Felt Hat',
    searchable_by=['Pikachu with Grey Felt Hat', 'Basic', 'PikachuwithGreyFeltHat'],
    subtypes=['Basic'],
    collector_number=85,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=25,
    abilities=[
        Attack(
            title='Pika-Portrait',
            game_text='Search your deck for a Pikachu and put it onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
    ],
)
