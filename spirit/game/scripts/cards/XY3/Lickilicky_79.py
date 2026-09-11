from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d0fb4bc1-3af5-5da9-8334-7ed237369479',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lickilicky.Name',
    display_name='Lickilicky',
    searchable_by=['Lickilicky', 'Stage 1', 'Lickilicky'],
    subtypes=['Stage 1'],
    collector_number=79,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name',
    family_id=108,
    abilities=[
        Attack(
            title='Knock Off',
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Lickichop',
            game_text='Flip a coin until you get tails. This attack does 30 more damage for each heads.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
