from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2250323f-e071-50cd-bc8c-647a8fea7add',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Persian.Name',
    display_name='Persian',
    searchable_by=['Persian', 'Stage 1', 'Persian'],
    subtypes=['Stage 1'],
    collector_number=126,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name',
    family_id=52,
    abilities=[
        Attack(
            title="Make 'Em Pay",
            game_text='If your opponent has 4 or more cards in their hand, they reveal their hand. Discard cards you find there until your opponent has exactly 4 cards in their hand.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Sharp Claws',
            game_text='Flip a coin. If heads, this attack does 60 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
