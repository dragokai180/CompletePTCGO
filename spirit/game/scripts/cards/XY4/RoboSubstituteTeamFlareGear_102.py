from spirit.game.data_utils import Ability, Activations, FossilItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_passive,
)


_TEXT = "Play this card as if it were a 30 HP Colorless Basic Pokémon. At any time during your turn (before your attack), you may discard this card from play. This card can't retreat. If this card is Knocked Out, your opponent can't take any Prize Cards for it. You may play as many Item cards as you like during your turn (before your attack)."

card = FossilItemCardDef(
    guid='8457bcad-af76-541d-a184-e2d862a64b72',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.RoboSubstituteTeamFlareGear.Name',
    display_name='Robo Substitute Team Flare Gear',
    searchable_by=['Robo Substitute Team Flare Gear', 'Item', 'RoboSubstituteTeamFlareGear'],
    subtypes=['Item'],
    collector_number=102,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=30,
    passive=standard_passive(_TEXT),
    abilities=[Ability(
        title="Discard Robo Substitute",
        is_rule_action=True,
        game_text=_TEXT,
        effect=standard_ability,
        activation=Activations.UNLIMITED,
    )],
)
