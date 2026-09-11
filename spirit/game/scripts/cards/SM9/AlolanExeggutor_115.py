from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='df0eccc8-b3b6-5c4b-b304-0b83d7380a5c',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanExeggutor.Name',
    display_name='Alolan Exeggutor',
    searchable_by=['Alolan Exeggutor', 'Stage 1', 'AlolanExeggutor'],
    subtypes=['Stage 1'],
    collector_number=115,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name',
    family_id=102,
    abilities=[
        Attack(
            title='Paradise Draw',
            game_text='You may discard any number of cards from your hand. Then, draw cards until you have 6 cards in your hand.',
            cost={},
            effect=standard_attack,
        ),
        Attack(
            title='Egg Splat',
            game_text='Discard any number of Exeggcute from your hand. This attack does 60 damage for each card you discarded in this way.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
