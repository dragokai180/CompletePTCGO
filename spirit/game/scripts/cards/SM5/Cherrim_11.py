from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='afd2fde3-1be2-5b36-bb61-595e7a85f6a7',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cherrim.Name',
    display_name='Cherrim',
    searchable_by=['Cherrim', 'Stage 1', 'Cherrim'],
    subtypes=['Stage 1'],
    collector_number=11,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cherubi.Name',
    family_id=420,
    abilities=[
        Ability(
            title='Weather Guard',
            game_text='Your Grass Pokémon have no Weakness.',
            passive=standard_passive('Your Grass Pokémon have no Weakness.'),
        ),
        Attack(
            title='Seed Bomb',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
    ],
)
