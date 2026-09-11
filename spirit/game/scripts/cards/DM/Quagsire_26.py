from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9ecb7535-5245-5f5f-b056-c3f30abea386',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Quagsire.Name',
    display_name='Quagsire',
    searchable_by=['Quagsire', 'Stage 1', 'Quagsire'],
    subtypes=['Stage 1'],
    collector_number=26,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name',
    family_id=194,
    abilities=[
        Ability(
            title='Wash Out',
            game_text='As often as you like during your turn (before your attack), you may move a Water Energy from 1 of your Benched Pokémon to your Active Pokémon.',
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title='Hydro Pump',
            game_text='This attack does 20 more damage times the amount of Water Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
