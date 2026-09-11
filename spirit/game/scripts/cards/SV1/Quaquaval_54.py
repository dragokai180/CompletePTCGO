from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8e535226-93e4-5e35-91ae-ab6274016ca5',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Quaquaval.Name',
    display_name='Quaquaval',
    searchable_by=['Quaquaval', 'Stage 2', 'Quaquaval'],
    subtypes=['Stage 2'],
    collector_number=54,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Quaxwell.Name',
    family_id=912,
    abilities=[
        Ability(
            title='Energy Carnival',
            game_text='Once during your turn, you may attach a Basic Energy card from your hand to 1 of your Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Hydro Kick',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)
