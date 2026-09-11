from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='aeb91487-7dc7-558b-8053-e58d95e09ccd',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aegislash.Name',
    display_name='Aegislash',
    searchable_by=['Aegislash', 'Stage 2', 'Aegislash'],
    subtypes=['Stage 2'],
    collector_number=49,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name',
    family_id=679,
    abilities=[
        Attack(
            title='Ticking Knock Out',
            game_text='During your next turn, if the Defending Pokémon is damaged by an attack, it will be Knocked Out.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Draining Blade',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 3},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
