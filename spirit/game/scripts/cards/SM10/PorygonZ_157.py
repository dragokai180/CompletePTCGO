from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='32586312-1995-595f-a63f-0d71fdf19402',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name',
    display_name='Porygon-Z',
    searchable_by=['Porygon-Z', 'Stage 2', 'PorygonZ'],
    subtypes=['Stage 2'],
    collector_number=157,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name',
    family_id=137,
    abilities=[
        Ability(
            title='Crazy Code',
            game_text='As often as you like during your turn (before your attack), you may attach a Special Energy card from your hand to 1 of your Pokémon.',
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title='Tantrum',
            game_text='This Pokémon is now Confused.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
