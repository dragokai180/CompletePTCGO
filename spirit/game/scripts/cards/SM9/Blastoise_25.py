from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='efe4757a-12fc-59b7-b4df-26e5c4195fa3',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Blastoise.Name',
    display_name='Blastoise',
    searchable_by=['Blastoise', 'Stage 2', 'Blastoise'],
    subtypes=['Stage 2'],
    collector_number=25,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name',
    family_id=7,
    abilities=[
        Ability(
            title='Powerful Squall',
            game_text='Once during your turn (before your attack), you may look at the top 6 cards of your deck and attach any number of Water Energy cards you find there to your Pokémon in any way you like. Shuffle the other cards back into your deck.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Hydro Tackle',
            game_text='This Pokémon does 30 damage to itself.',
            cost={PokemonTypes.WATER: 3},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
