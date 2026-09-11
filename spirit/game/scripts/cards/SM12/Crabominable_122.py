from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f8c3a0df-6183-586c-96cb-1e7baf631d9c',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Crabominable.Name',
    display_name='Crabominable',
    searchable_by=['Crabominable', 'Stage 1', 'Crabominable'],
    subtypes=['Stage 1'],
    collector_number=122,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name',
    family_id=739,
    abilities=[
        Ability(
            title='Solid Shell',
            game_text='This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).',
            passive=standard_passive('This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Freezing Punch',
            game_text='If this Pokémon has any Water Energy attached to it, this attack does 80 more damage.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
