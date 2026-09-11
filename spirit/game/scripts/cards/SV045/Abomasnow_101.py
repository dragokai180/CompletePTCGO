from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8a226859-5298-5828-831a-66e4dbccc76c',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Abomasnow.Name',
    display_name='Abomasnow',
    searchable_by=['Abomasnow', 'Stage 1', 'Abomasnow'],
    subtypes=['Stage 1'],
    collector_number=101,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name',
    family_id=459,
    abilities=[
        Ability(
            title='Freezing Disaster',
            game_text="Pokémon (both yours and your opponent's) can't be healed.",
            passive=standard_passive("Pokémon (both yours and your opponent's) can't be healed."),
        ),
        Attack(
            title='Magnum Punch',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)
