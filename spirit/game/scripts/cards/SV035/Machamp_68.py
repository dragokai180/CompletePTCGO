from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='80035623-1c02-5635-8182-3fea8432cd4b',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name',
    display_name='Machamp',
    searchable_by=['Machamp', 'Stage 2', 'Machamp'],
    subtypes=['Stage 2'],
    collector_number=68,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name',
    family_id=66,
    abilities=[
        Ability(
            title='Guts',
            game_text='If this Pokémon would be Knocked Out by damage from an attack, flip a coin. If heads, this Pokémon is not Knocked Out, and its remaining HP becomes 10.',
            passive=standard_passive('If this Pokémon would be Knocked Out by damage from an attack, flip a coin. If heads, this Pokémon is not Knocked Out, and its remaining HP becomes 10.'),
        ),
        Attack(
            title='Mountain Chopping',
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
