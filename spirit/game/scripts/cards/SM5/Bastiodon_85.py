from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='be6c11c6-bc94-5e1a-8a69-97275e9dee01',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bastiodon.Name',
    display_name='Bastiodon',
    searchable_by=['Bastiodon', 'Stage 2', 'Bastiodon'],
    subtypes=['Stage 2'],
    collector_number=85,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name',
    family_id=410,
    abilities=[
        Ability(
            title='Earthen Shield',
            game_text="Prevent all damage done to your Metal Pokémon by attacks from your opponent's Pokémon that have any Special Energy attached to them.",
            passive=standard_passive("Prevent all damage done to your Metal Pokémon by attacks from your opponent's Pokémon that have any Special Energy attached to them."),
        ),
        Attack(
            title='Push Down',
            game_text='You may have your opponent switch their Active Pokémon with 1 of their Benched Pokémon.',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
