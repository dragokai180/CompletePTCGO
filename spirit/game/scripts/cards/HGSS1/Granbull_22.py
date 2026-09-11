from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0f498616-94f2-572b-ab68-b0b49c41bcd4',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Granbull.Name',
    display_name='Granbull',
    searchable_by=['Granbull', 'Stage 1', 'Granbull'],
    subtypes=['Stage 1'],
    collector_number=22,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name',
    family_id=209,
    abilities=[
        Attack(
            title='Timid Tackle',
            game_text='Granbull does 20 damage to itself. Switch Granbull with 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Chomp',
            game_text='Does 40 damage plus 10 more damage for each damage counter on Granbull.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
