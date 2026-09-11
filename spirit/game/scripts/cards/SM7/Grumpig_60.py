from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8a406548-3740-5df9-b05d-87aefd61df76',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Grumpig.Name',
    display_name='Grumpig',
    searchable_by=['Grumpig', 'Stage 1', 'Grumpig'],
    subtypes=['Stage 1'],
    collector_number=60,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name',
    family_id=325,
    abilities=[
        Attack(
            title='Mirror Step',
            game_text="If 1 of your opponent's Pokémon in play has the same name as 1 of your Pokémon in play, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
