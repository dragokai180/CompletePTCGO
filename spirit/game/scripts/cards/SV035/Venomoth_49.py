from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='58b38e1d-5fdd-5e6c-ac35-116176b26d48',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Venomoth.Name',
    display_name='Venomoth',
    searchable_by=['Venomoth', 'Stage 1', 'Venomoth'],
    subtypes=['Stage 1'],
    collector_number=49,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name',
    family_id=48,
    abilities=[
        Attack(
            title='Perplexing Powder',
            game_text="Your opponent's Active Pokémon is now Confused. During your opponent's next turn, they can't play any Item cards from their hand.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Speed Wing',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
