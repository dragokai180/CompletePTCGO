from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bdc28478-cc70-5ac2-9dca-0dc2b9e2de0f',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golisopod.Name',
    display_name='Golisopod',
    searchable_by=['Golisopod', 'Stage 1', 'Golisopod'],
    subtypes=['Stage 1'],
    collector_number=51,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name',
    family_id=767,
    abilities=[
        Ability(
            title='Emergency Exit',
            game_text='If this Pokémon has 2 or fewer Energy attached to it, it has no Retreat Cost.',
            passive=standard_passive('If this Pokémon has 2 or fewer Energy attached to it, it has no Retreat Cost.'),
        ),
        Attack(
            title='First Impression',
            game_text='If this Pokémon was on the Bench and became your Active Pokémon this turn, this attack does 60 more damage.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
