from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f141acdb-fa93-5a3f-af03-b9b4821c133a',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name',
    display_name='Blissey',
    searchable_by=['Blissey', 'Stage 1', 'Blissey'],
    subtypes=['Stage 1'],
    collector_number=56,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name',
    family_id=242,
    abilities=[
        Attack(
            title='Double Slap',
            game_text='Flip 2 coins. This attack does 40 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title="Nurse's Egg",
            game_text='Heal 100 damage from each of your Benched Pokémon. Then, discard 2 Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 4},
            effect=standard_attack,
        ),
    ],
)
