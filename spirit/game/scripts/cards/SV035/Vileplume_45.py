from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d3ab283a-5f01-5f59-8c9d-852a9b8d65ee',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name',
    display_name='Vileplume',
    searchable_by=['Vileplume', 'Stage 2', 'Vileplume'],
    subtypes=['Stage 2'],
    collector_number=45,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name',
    family_id=43,
    abilities=[
        Ability(
            title='Fully Blooming Energy',
            game_text='When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may look at the top 8 cards of your deck and attach any number of Basic Energy cards you find there to your Pokémon in any way you like. Shuffle the other cards back into your deck.',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Solar Beam',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
