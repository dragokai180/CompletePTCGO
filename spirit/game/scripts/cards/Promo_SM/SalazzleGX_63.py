from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9361b5f7-9e9e-5175-afbd-49d70cd95f24',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SalazzleGX.Name',
    display_name='Salazzle-GX',
    searchable_by=['Salazzle-GX', 'Stage 1', 'GX', 'SalazzleGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=63,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name',
    family_id=757,
    abilities=[
        Attack(
            title='Diabolical Claws',
            game_text='This attack does 50 damage for each Prize card you have taken.',
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Heat Blast',
            cost={PokemonTypes.FIRE: 2},
            damage=110,
        ),
        Attack(
            title="Queen's Haze-GX",
            game_text="Discard all Energy from your opponent's Active Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 2},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
