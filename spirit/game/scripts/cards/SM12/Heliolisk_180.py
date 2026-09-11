from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bef72908-6d50-52fd-a28b-4f5798498cec',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Heliolisk.Name',
    display_name='Heliolisk',
    searchable_by=['Heliolisk', 'Stage 1', 'Heliolisk'],
    subtypes=['Stage 1'],
    collector_number=180,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name',
    family_id=694,
    abilities=[
        Attack(
            title='Parabolic Counter',
            game_text='If your opponent has any Lightning Pokémon in play, this attack does 90 more damage.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Zap Kick',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
