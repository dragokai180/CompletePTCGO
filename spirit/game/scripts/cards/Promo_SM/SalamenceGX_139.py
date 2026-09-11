from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='65016ed8-db8e-5ff2-aab0-94f787cd7ee7',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SalamenceGX.Name',
    display_name='Salamence-GX',
    searchable_by=['Salamence-GX', 'Stage 2', 'GX', 'SalamenceGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=139,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name',
    family_id=373,
    abilities=[
        Ability(
            title='Dragon Lift',
            game_text='Your Pokémon in play have no Retreat Cost, except Pokémon-GX and Pokémon-EX.',
            passive=standard_passive('Your Pokémon in play have no Retreat Cost, except Pokémon-GX and Pokémon-EX.'),
        ),
        Attack(
            title='Bright Flame',
            game_text='Discard 2 Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=standard_attack,
        ),
        Attack(
            title='Flame Jet-GX',
            game_text="This attack does 120 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
