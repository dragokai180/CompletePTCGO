from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='94cabe85-a47e-51b2-aa46-3470910f6073',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name',
    display_name='Exeggutor',
    searchable_by=['Exeggutor', 'Stage 1', 'Exeggutor'],
    subtypes=['Stage 1'],
    collector_number=18,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name',
    family_id=102,
    abilities=[
        Attack(
            title='Energy Absorption',
            game_text='Search your discard pile for up to 2 Energy cards and attach them to Exeggutor.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Big Eggsplosion',
            game_text='Flip a coin for each Energy attached to Exeggutor. This attack does 40 damage times the number of heads.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
