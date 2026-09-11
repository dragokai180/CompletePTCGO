from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ab6584ad-f5f2-5778-ad46-3912fc65cd68',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Arboliva.Name',
    display_name='Arboliva',
    searchable_by=['Arboliva', 'Stage 2', 'Arboliva'],
    subtypes=['Stage 2'],
    collector_number=23,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dolliv.Name',
    family_id=928,
    abilities=[
        Ability(
            title='Enriching Oil',
            game_text='When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may heal all damage from 1 of your Pokémon.',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Solar Beam',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
        ),
    ],
)
