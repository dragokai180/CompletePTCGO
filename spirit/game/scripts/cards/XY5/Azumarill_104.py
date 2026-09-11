from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bde49eae-ad30-575b-a96f-cf2d38b00d01',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name',
    display_name='Azumarill',
    searchable_by=['Azumarill', 'Stage 1', 'Azumarill'],
    subtypes=['Stage 1'],
    collector_number=104,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name',
    family_id=183,
    abilities=[
        Attack(
            title='Tail Rap',
            game_text='Flip 2 coins. This attack does 30 damage times the number of heads.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Dwindling Wave',
            game_text='This attack does 100 damage minus 10 damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator='-',
            effect=standard_attack,
        ),
    ],
    passive=standard_passive('When this Pokémon is healed, double the amount healed.'),
)
