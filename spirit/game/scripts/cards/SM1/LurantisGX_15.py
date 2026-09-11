from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9805df94-93c3-5845-8346-01b708257d0d',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.LurantisGX.Name',
    display_name='Lurantis-GX',
    searchable_by=['Lurantis-GX', 'Stage 1', 'GX', 'LurantisGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=15,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Fomantis.Name',
    family_id=753,
    abilities=[
        Attack(
            title='Flower Supply',
            game_text='Attach 2 basic Energy cards from your discard pile to your Pokémon in any way you like.',
            cost={PokemonTypes.GRASS: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Solar Blade',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
        Attack(
            title='Chloroscythe-GX',
            game_text="This attack does 50 damage times the amount of Grass Energy attached to this Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
            gx=True,
        ),
    ],
)
