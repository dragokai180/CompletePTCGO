from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b5a90365-8e0e-5edc-8e85-95dd4f6d333a',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PrimarinaGX.Name',
    display_name='Primarina-GX',
    searchable_by=['Primarina-GX', 'Stage 2', 'GX', 'PrimarinaGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=42,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=250,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Brionne.Name',
    family_id=728,
    abilities=[
        Attack(
            title='Bubble Beat',
            game_text='This attack does 20 more damage times the amount of Water Energy attached to your Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Roaring Seas',
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
        Attack(
            title='Grand Echo-GX',
            game_text="Heal all damage from all of your Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
