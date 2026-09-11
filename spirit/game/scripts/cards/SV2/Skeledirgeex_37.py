from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='819d6db4-612e-521d-9fce-808c8df494cf',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skeledirgeex.Name',
    display_name='Skeledirge ex',
    searchable_by=['Skeledirge ex', 'Stage 2', 'ex', 'Skeledirgeex'],
    subtypes=['Stage 2', 'ex'],
    collector_number=37,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Crocalor.Name',
    family_id=909,
    abilities=[
        Attack(
            title='Vitality Song',
            game_text='Heal 30 damage from each of your Pokémon.',
            cost={PokemonTypes.FIRE: 1},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Burning Voice',
            game_text='This attack does 10 less damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.FIRE: 2},
            damage=270,
            damage_operator='-',
            effect=standard_attack,
        ),
    ],
)
