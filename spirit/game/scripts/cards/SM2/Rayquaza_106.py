from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='21a380f8-2e94-5d73-ba05-0437b7d1e237',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name',
    display_name='Rayquaza',
    searchable_by=['Rayquaza', 'Basic', 'Rayquaza'],
    subtypes=['Basic'],
    collector_number=106,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=384,
    abilities=[
        Attack(
            title='Turbo Storm',
            game_text='Attach 2 basic Energy cards from your discard pile to 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Dragon Claw',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
