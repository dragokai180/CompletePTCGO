from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='691bfab2-289f-5529-8e31-ad863c44e23d',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name',
    display_name='Volcarona',
    searchable_by=['Volcarona', 'Stage 1', 'Volcarona'],
    subtypes=['Stage 1'],
    collector_number=41,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name',
    family_id=636,
    abilities=[
        Attack(
            title='Flame Cloak',
            game_text='Attach a Basic Fire Energy card from your discard pile to this Pokémon.',
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Heat Blast',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
