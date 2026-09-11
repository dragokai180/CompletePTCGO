from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5aa08e60-3553-5920-bdb0-8fbf83982b8e',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kabutops.Name',
    display_name='Kabutops',
    searchable_by=['Kabutops', 'Stage 2', 'Kabutops'],
    subtypes=['Stage 2'],
    collector_number=141,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name',
    family_id=140,
    abilities=[
        Ability(
            title='Ancient Way',
            game_text="Apply Weakness for your opponent's Active Pokémon as ×4 instead.",
            passive=standard_passive("Apply Weakness for your opponent's Active Pokémon as ×4 instead."),
        ),
        Attack(
            title='Draining Blade',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
