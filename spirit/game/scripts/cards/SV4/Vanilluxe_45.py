from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='405b0555-30f1-5ad8-9bee-31c5fd1ceeca',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vanilluxe.Name',
    display_name='Vanilluxe',
    searchable_by=['Vanilluxe', 'Stage 2', 'Vanilluxe'],
    subtypes=['Stage 2'],
    collector_number=45,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name',
    family_id=582,
    abilities=[
        Ability(
            title='Frigid Room',
            game_text="Your opponent's Pokémon that have 40 HP or less remaining can't attack.",
            passive=standard_passive("Your opponent's Pokémon that have 40 HP or less remaining can't attack."),
        ),
        Attack(
            title='Icicle Missile',
            cost={PokemonTypes.WATER: 2},
            damage=110,
        ),
    ],
)
