from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e8dde8ea-20de-5caf-b8a8-a175a934cd64',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name',
    display_name='Raticate',
    searchable_by=['Raticate', 'Stage 1', 'Raticate'],
    subtypes=['Stage 1'],
    collector_number=34,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name',
    family_id=19,
    abilities=[
        Attack(
            title='Razor-Sharp Incisors',
            game_text='Does 10 damage times the number of damage counters on the Defending Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Gnaw Up',
            game_text='Discard a Special Energy card attached to the Defending Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
