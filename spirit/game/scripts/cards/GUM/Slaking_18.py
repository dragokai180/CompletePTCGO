from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='24a91ca8-c661-597a-aae4-588f2c7b6e39',
    key='GUM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slaking.Name',
    display_name='Slaking',
    searchable_by=['Slaking', 'Stage 2', 'Slaking'],
    subtypes=['Stage 2'],
    collector_number=18,
    set_code='GUM',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name',
    family_id=289,
    abilities=[
        Attack(
            title='Pitch',
            game_text='Your opponent switches their Active Pokémon with 1 of their Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
