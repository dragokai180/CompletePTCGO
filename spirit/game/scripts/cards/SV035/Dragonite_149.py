from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5e44d9a9-3a20-5e52-b302-1ac96d166e5a',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name',
    display_name='Dragonite',
    searchable_by=['Dragonite', 'Stage 2', 'Dragonite'],
    subtypes=['Stage 2'],
    collector_number=149,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name',
    family_id=147,
    abilities=[
        Ability(
            title='Jet Cruise',
            game_text='Your Pokémon in play have no Retreat Cost.',
            passive=standard_passive('Your Pokémon in play have no Retreat Cost.'),
        ),
        Attack(
            title='Dragon Pulse',
            game_text='Discard the top 2 cards of your deck.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=180,
            effect=standard_attack,
        ),
    ],
)
